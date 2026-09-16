import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2, ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

def create_model(model_name="MobileNetV2", num_classes=38):
    input_shape = (224, 224, 3)
    
    # Load Pre-trained Base Model
    if model_name == "MobileNetV2":
        base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=input_shape)
    elif model_name == "ResNet50":
        base_model = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)
    else:
        raise ValueError("Model not supported in this prototype.")
        
    # Freeze base model layers to prevent catastrophic forgetting
    for layer in base_model.layers:
        layer.trainable = False

    # Add custom classification head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.5)(x)
    predictions = Dense(num_classes, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Compile the model
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
                  loss='categorical_crossentropy',
                  metrics=['accuracy', tf.keras.metrics.Precision(name="precision"), tf.keras.metrics.Recall(name="recall")])
    return model

if __name__ == "__main__":
    print("🌿 Initializing Plant Disease Detection Model...")
    
    # Example: Create the optimal model from our research paper
    model = create_model("MobileNetV2", num_classes=38)
    model.summary()
    
    print("\n✅ Model structure ready.")
    print("To train, load the PlantVillage dataset (e.g., using tf.keras.preprocessing.image_dataset_from_directory)")
    print("Example snippet:")
    print("train_ds = tf.keras.preprocessing.image_dataset_from_directory('path_to_dataset', image_size=(224, 224), batch_size=32)")
    print("model.fit(train_ds, epochs=50)")
