from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector

class ActionFetchFromDatabase(Action):

    def name(self) -> Text:
        return "action_fetch_from_database"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='efdrpdr-cname.us.dell.com',
            user='',
            password='your_mysql_password',
            database='your_database_name'
        )

        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT your_column FROM your_table WHERE condition")

        # Fetch the results
        results = cursor.fetchall()

        # Close the connection
        cursor.close()
        connection.close()

        # Process the results and send a message to the user
        if results:
            result_string = ', '.join([str(result[0]) for result in results])
            dispatcher.utter_message(text=f"Here are the results: {result_string}")
        else:
            dispatcher.utter_message(text="No results found.")

        return []



# class ActionSayPhone(Action):
#     def name(self)-> Text:
#         return "action_say_phone"

# def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain:  Dict[Text,Any]) ->List[Dict[Text, Any]] :


#              phone= tracker.get_slot("phone")

#              if not phone:
#                  dispatcher.utter_message(text="Sorry i don't know your number")
#              else:
#                  dispatcher.utter_message(text=f"Your phone number is(phone)") 
             
             
#              return[]          