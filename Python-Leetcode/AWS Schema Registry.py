import boto3
import json
import fastavro
from fastavro import writer, parse_schema

def get_latest_schema(registry_name, schema_name):
    """Fetches the latest schema version from AWS Glue Schema Registry."""
    glue_client = boto3.client('glue')
    response = glue_client.get_schema_version(
        SchemaId={'RegistryName': registry_name, 'SchemaName': schema_name},
        SchemaVersionNumber={'LatestVersion': True}
    )
    schema_definition = response['SchemaDefinition']
    print("Retrieved Schema Definition:", schema_definition)  # Debugging
    
    # Parse using json.loads for initial loading
    parsed_schema = json.loads(schema_definition) 
    
    # Convert to fastavro's schema format
    fastavro_schema = parse_schema(parsed_schema)  

    return fastavro_schema

def serialize_product_data(product_data, schema):
    """Serializes product data to Avro format based on the given schema."""
    with open("products.avro", "wb") as out_file:
        fastavro.writer(out_file, schema, product_data)
        
def deserialize_product_data(file_path, schema):
    """Deserializes product data from an Avro file based on the given schema."""
    with open(file_path, "rb") as avro_file:
        for product in fastavro.reader(avro_file, reader_schema=schema):
            print(product)


# Load your product data (replace with your actual data source)
product_data = [
    {"productId": "1", "productName": "Laptop", "productPrice": 999.99},
    {"productId": "2", "productName": "Smartphone", "productPrice": 599.99},
]

# Get the latest schema from the registry
schema = get_latest_schema("product-catalog-registry", "product-schema")  

# Serialize the product data
# serialize_product_data(product_data, schema)
# deserialize_product_data("products.avro", schema)

print(schema)

# print("Serialized product data written to products.avro")
