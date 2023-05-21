#Importing the product recommender function from use.py
from use import product_recommender
#import FastAPI
from fastapi import APIRouter, Form, Response, status

router = APIRouter()
@router.post("/clothing/similarity_search")
#Create function for taking input query and giving output in json format
def food_detector(query: str = Form(...),
                  response: Response = None):  # type: ignore
    try:
        top_products_list=product_recommender(query)
        output={"similar_products":top_products_list}
        return output
   
    except Exception as e:
        resp = {
            'status': 500,
            'message': f"Something went wrong !! ({type(e)} | {e} | {e.args})"
        }
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return resp