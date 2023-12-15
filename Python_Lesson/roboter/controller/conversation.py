"""Controller for speaking with robot"""
from roboter.models import robot # roboter.models.robot


def talk_about_restaurant(): # レストランについて話す
    """Function to speak with robot""" # ロボットと話す関数
    restaurant_robot = robot.RestaurantRobot() # roboter.models.robot.RestaurantRobot()
    restaurant_robot.hello() # 挨拶をする
    restaurant_robot.recommend_restaurant()  # レストランを勧める
    restaurant_robot.ask_user_favorite()   # ユーザーの好みを聞く   
    restaurant_robot.thank_you()  # ありがとうを言う

