import json
import os 
from typing import List, Dict

DATA_FILE = "data/products.json"

def load_products() -> List[Dict]:
    """
    Charge la liste des produits du fichier JSON

    Returns :
        List[Dict]: Liste des produits sous form de disctionnaire
    """
    try :
        # verifier que le fichier existe

        if not os.path.exists(DATA_FILE) :
            return []
        
        with open(DATA_FILE, 'r', encoding="utf-8") as file :
            products = json.load(file)
            return(products)

    except json.JSONDecodeError:
        print("erreur le fichier JSON est corrompu")
        return []
    except Exception as e:
        print(f"Erreur lors du chargement des produits : {e}")
        return[]

def save_products(products:List[Dict]) -> None:
    """
    ajouter un produit la liste de produits
    """
    try :
        # verifier que le fichier existe

        if os.path.exists(DATA_FILE) :
            with open(DATA_FILE, 'w', encoding="utf-8") as outfile:
                json.dump(products, outfile, indent=4)
                print(products)
        
    except json.JSONDecodeError:
        print("erreur le fichier JSON est corrompu")
    except Exception as e:
        print(f"Erreur lors de la lecture de la liste des produits : {e}")
    
def generate_id(products: List[Dict]) -> int:

    """
    generer l'id du futur produit ajouté

    Returns :
        int
    """
    try :
            if len(products) == 0 or products == None :
                return 0
            products_ids = [product ["id"] for product in products]
            max_id = max(products_ids)
            return max_id + 1
            
    except json.JSONDecodeError:
        print("erreur le fichier JSON est corrompu")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture de la liste des produits : {e}")
        return[]


if __name__ == "__main__":
    products = load_products()

    id_product_added = generate_id(products)
    name_product_added = "clavier mecanique"
    description_product_added = "Clavier m\u00e9canique RGB, switches Cherry MX"
    price_product_added = 149.99
    stock_product_added = 8
    
    productadded = {"id": id_product_added, "name": name_product_added, "description": description_product_added, "price": price_product_added, "stock": stock_product_added}
    products.append(productadded)

    save_products(products)