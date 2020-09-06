# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk.forms import FormAction

class LavarForm(FormAction):
    """ Pregunta la información sobre la ropa que se quiere lavar"""

    def name(self) -> Text:
        return "lavar_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ La lista de espacios a llenar de lavar_form"""
        return [
            "tipo_prenda",
            "numero_prendas",
            "tipo_lavado"
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Entendido. ¿Te gustaría que recolectemos tus prendas a domicilio o prefieres pasar a sucursal?")
        return []
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {
            "numero_prendas": [
                self.from_entity(entity="number"),

            ]
        }
class PlancharForm(FormAction):
    """ Pregunta la información sobre la ropa que se quiere planchar"""

    def name(self) -> Text:
        return "planchar_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ La lista de espacios a llenar de planchar_form"""
        return [
            "tipo_prenda",
            "numero_prendas",
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Entendido. ¿Te gustaría que recolectemos tus prendas a domicilio o prefieres pasar a sucursal?")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {
            "numero_prendas": [
                self.from_entity(entity="number"),

            ]
        }

class ComponerForm(FormAction):
    """ Pregunta la información sobre la ropa que se quiere componer"""

    def name(self) -> Text:
        return "componer_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ La lista de espacios a llenar de componer_form"""
        return [
            "tipo_prenda",
            "tipo_compostura"
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Entendido. ¿Te gustaría que recolectemos tu prenda a domicilio o prefieres pasar a sucursal?")
        return []

class DomicilioForm(FormAction):
    """ Pregunta la información sobre el domicilio y fecha hora para recolectar las prendas"""

    def name(self) -> Text:
        return "domicilio_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ La lista de espacios a llenar de domicilio_form"""
        return [
            "domicilio",
            "fecha_hora"
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Muy bien, te visitaremos en la fecha y hora acordada.")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {
            "fecha_hora": [
                self.from_entity(entity="time"),

            ]
        }

class SucursalForm(FormAction):
    """ Pregunta la información sobre el domicilio y fecha hora para recolectar las prendas"""

    def name(self) -> Text:
        return "sucursal_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """ La lista de espacios a llenar de sucursal_form"""
        return [
            "sucursal",
            "fecha_hora"
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Muy bien, te esperamos en nuestra sucursal en la fecha y hora acordada.")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {
            "fecha_hora": [
                self.from_entity(entity="time"),

            ]
        }


from rasa_sdk.events import UserUtteranceReverted
class ActionSaludarUsuario(Action):
    """Volver al estado de la conversación cuando el usuario salude de nuevo por alguna razón"""

    def name(self) -> Text:
        return "action_saludar"

    def run(
        self,
        dispatcher,
        tracker,
        domain
    ):
        dispatcher.utter_template("utter_saludar", tracker)
        return [UserUtteranceReverted()]

class ActionBotChallenge(Action):
    """Volver al estado de la conversación cuando el usuario pregunte con quién habla"""

    def name(self) -> Text:
        return "action_bot"

    def run(
        self,
        dispatcher,
        tracker,
        domain
    ):
        dispatcher.utter_template("utter_soyunbot", tracker)
        return [UserUtteranceReverted()]
