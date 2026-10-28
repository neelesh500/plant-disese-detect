            except Exception:
                return jsonify({"error": "Invalid or unreadable image file."}), 400
            image = image.resize((224, 224))
            img_array = np.array(image) / 255.0  # Normalize to [0, 1]
            img_array = np.expand_dims(img_array, axis=0) # Shape: (1, 224, 224, 3)
            
            # Use only the model's trained class mapping; never guess class labels.
            if model is None:
                return jsonify({"error": "No trained model is available. Configure a trained ONNX model."}), 503
            try:
                if hasattr(model, 'run'):
                    img_array_f32 = img_array.astype(np.float32)
                    model_input = model.get_inputs()[0]
                    input_name = model_input.name
                    input_shape = model_input.shape
                    if len(input_shape) != 4:
                        raise ValueError("Model input must have four dimensions")
                    if input_shape[1] == 3 and input_shape[2] == 224 and input_shape[3] == 224:
                        img_array_f32 = np.transpose(img_array_f32, (0, 3, 1, 2))
                    elif input_shape[1] not in (3, "3") or input_shape[2] not in (224, "224") or input_shape[3] not in (224, "224"):
                        if input_shape[1] not in (224, "224") or input_shape[2] not in (224, "224") or input_shape[3] not in (3, "3"):
                            raise ValueError("Model input dimensions are incompatible with 224x224 RGB preprocessing")
                    preds = model.run(None, {input_name: img_array_f32})[0]
                else:
                    preds = model.predict(img_array, verbose=0)
                scores = np.asarray(preds)
                if scores.ndim != 2 or scores.shape[0] != 1 or scores.shape[1] == 0:
                    raise ValueError("Invalid model output shape")
                names_path = os.path.join("models", "class_names.json")
                if not os.path.exists(names_path):
                    return jsonify({"error": "Trained model class mapping (models/class_names.json) is missing."}), 503
                with open(names_path, "r", encoding="utf-8") as names_file:
                    class_names = json.load(names_file)
                if not isinstance(class_names, list) or len(class_names) != scores.shape[1]:
                    return jsonify({"error": "Model output dimensions do not match models/class_names.json."}), 503
                class_idx = int(np.argmax(scores[0]))
                disease_name = str(class_names[class_idx])
                confidence = float(scores[0][class_idx]) * 100
                treatment = "Consult a local plant health specialist for treatment guidance."
            except Exception as e:
                logger.error("Error during prediction: %s", e)
                return jsonify({"error": "Inference failed. Check the uploaded image and model configuration."}), 500

            # Calculate actual processing latency
            latency_ms = int((time.time() - start_time) * 1000)

            response = {
                "disease": disease_name.replace("_", " ").title(),
                "treatment": treatment,
                "confidence": f"{confidence:.2f}",
                "latency": f"{latency_ms}",
                "severity_percentage": None
            }

            return jsonify(response)

        return jsonify({"error": "Invalid file type"}), 400
    except Exception as e:
        logger.error("Error in prediction pipeline: %s", e)
        return jsonify({"error": "Unable to process this image. Check the file and model configuration."}), 500

@app.route("/api/agent", methods=["POST"])
def agent():
    data = request.get_json(silent=True) or {}
    query = data.get("query", "")
    if not isinstance(query, str):
        return jsonify({"error": "Query must be text."}), 400
    query = query.strip()

    if not query:
        return jsonify({"reply": "Please ask a question or give a command."}), 400
        
    try:
        api_key = os.environ.get("GEMINI_API_KEY") 
        model_name = os.environ.get("GEMINI_MODEL")
        if not api_key:
            return jsonify({"error": "Gemini is not configured: set GEMINI_API_KEY."}), 503
        if not model_name:
            return jsonify({"error": "Gemini is not configured: set GEMINI_MODEL to a supported model."}), 503
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        system_prompt = """
        You are AgriNet AI, an advanced agronomy and plant disease assistant.
        The user interacts with you through a voice and text interface.
        If the user asks to "open camera", "turn on camera", or similar UI action, reply EXACTLY AND ONLY WITH: [ACTION: CAMERA]
        If the user asks to "upload", "browse", or "select image", reply EXACTLY AND ONLY WITH: [ACTION: BROWSE]
        If the user asks to "analyze", "detect", "check disease", reply EXACTLY AND ONLY WITH: [ACTION: ANALYZE]
        If the user asks to "reset" or "clear", reply EXACTLY AND ONLY WITH: [ACTION: RESET]
        If the user asks to "close" or "shut down agent", reply EXACTLY AND ONLY WITH: [ACTION: CLOSE]
        Otherwise, answer their plant-related or farming-related question concisely in 1-2 sentences. Keep it very conversational and helpful. Do not use markdown format.
        """
        
        
        agent_model = genai.GenerativeModel(
            model_name,
            system_instruction=system_prompt
        )
        response = agent_model.generate_content(query)
        reply_text = (getattr(response, "text", None) or "").strip()
        if not reply_text:
            return jsonify({"error": "Gemini returned an empty response. Please try again."}), 502
        
        # Determine if it's an action
        action = None
        if "[ACTION: CAMERA]" in reply_text:
            action = "CAMERA"
            reply_text = "Opening camera. Say 'capture' or press the button to take a photo."
        elif "[ACTION: BROWSE]" in reply_text:
            action = "BROWSE"
            reply_text = "Opening file browser for you."
        elif "[ACTION: ANALYZE]" in reply_text:
            action = "ANALYZE"
            reply_text = "Initializing inference pipeline. Standardizing inputs now."
        elif "[ACTION: RESET]" in reply_text:
            action = "RESET"
            reply_text = "Resetting the workspace."
        elif "[ACTION: CLOSE]" in reply_text:
            action = "CLOSE"
            reply_text = "Goodbye! Closing AI Agent."
            
        return jsonify({"reply": reply_text, "action": action})
    
    except Exception as e:
        logger.error("Gemini API request failed: %s", type(e).__name__)
        return jsonify({"error": "Gemini request failed. Check the configured model and API availability."}), 502


