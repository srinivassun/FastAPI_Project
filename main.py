from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create FastAPI application
app = FastAPI(title="Product Management API")

# Pydantic Model

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str

# In-memory database

products = {
1: Product(id=1, name="Laptop", price=75000, category="Electronics"),
2: Product(id=2, name="Mobile", price=25000, category="Electronics"),
3: Product(id=3, name="Keyboard", price=1500, category="Accessories")
}

# 1. GET - Retrieve all products

@app.get("/products")
def get_products():
    return list(products.values())

# 2. GET - Retrieve product by ID

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    return products[product_id]


# 3. POST - Create a new product

@app.post("/products", status_code=201)
def create_product(product: Product):

    if product.id in products:
        raise HTTPException(status_code=409, detail="Product already exists")

    products[product.id] = product

    return {
        "message": "Product created successfully",
        "product": product
    }


# 4. PUT - Update an existing product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.id != product_id:
        raise HTTPException(status_code=400, detail="Product ID mismatch")

    products[product_id] = product

    return {
        "message": "Product updated successfully",
        "product": product
    }

# 5. PATCH - Partially update a product

@app.patch("/products/{product_id}")
def patch_product(product_id: int, product: dict):

    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_product = products[product_id].model_dump()

    updated_product = {**existing_product, **product}

    products[product_id] = Product(**updated_product)

    return {
        "message": "Product partially updated",
        "product": products[product_id]
    }


# 6. DELETE - Delete a product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")

    deleted_product = products.pop(product_id)

    return {
        "message": "Product deleted successfully",
        "product": deleted_product
    }


# Health check API

@app.get("/health")
def health_check():
    return {"status": "UP"}
