######################################################################################################################
#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.                                                #
#                                                                                                                    #
#  Licensed under the Apache License, Version 2.0 (the 'License'). You may not use this file except in compliance    #
#  with the License. A copy of the License is located at                                                             #
#                                                                                                                    #
#      http://www.apache.org/licenses/LICENSE-2.0                                                                    #
#                                                                                                                    #
#  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES #
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions    #
#  and limitations under the License.                                                                                #
######################################################################################################################
def slot_types(language):
    slot_type_values = {
        "English": [
            {"sampleValue": {"value": "cleaning"}},
            {"sampleValue": {"value": "root canal"}},
            {"sampleValue": {"value": "whitening"}},
        ],
        "French": [
            {"sampleValue": {"value": "nettoyage"}},
            {"sampleValue": {"value": "traitement du canal radiculaire"}},
            {"sampleValue": {"value": "blanchiment"}},
        ],
        "Italian": [
            {"sampleValue": {"value": "pulizia"}},
            {"sampleValue": {"value": "devitalizzazione"}},
            {"sampleValue": {"value": "blanchiment"}},
        ],
        "Spanish": [
            {"sampleValue": {"value": "limpieza"}},
            {"sampleValue": {"value": "endodoncia"}},
            {"sampleValue": {"value": "blanqueamiento"}},
        ],
        "German": [
            {"sampleValue": {"value": "Reinigung"}},
            {"sampleValue": {"value": "Wurzelbehandlung"}},
            {"sampleValue": {"value": "Wei??en"}},
        ],
        "Japanese": [
            {"sampleValue": {"value": "??????????????????"}},
            {"sampleValue": {"value": "????????????"}},
            {"sampleValue": {"value": "?????????????????????"}},
        ],
    }
    return slot_type_values[language]


def utterances(language):
    utterance_values = {
        "English": [
            {"utterance": "I would like to book an appointment"},
            {"utterance": "Book an appointment"},
            {"utterance": "Book a {AppointmentType}"},
        ],
        "French": [
            {"utterance": "Je souhaiterais prendre rendez-vous"},
            {"utterance": "Prendre rendez-vous"},
            {"utterance": "R??server un {AppointmentType}"},
        ],
        "Italian": [
            {"utterance": "Vorrei fissare un appuntamento"},
            {"utterance": "Fissa un appuntamento"},
            {"utterance": "Prenota un'operazione di {AppointmentType}"},
        ],
        "Spanish": [
            {"utterance": "Querr??a pedir una cita"},
            {"utterance": "Reservar una cita"},
            {"utterance": "Pedir cita para {AppointmentType}"},
        ],
        "German": [
            {"utterance": "Ich m??chte einen Termin buchen."},
            {"utterance": "Einen Termin buchen"},
            {"utterance": "Einen Termin des Typs {AppointmentType} buchen"},
        ],
        "Japanese": [
            {"utterance": "???????????????????????????"},
            {"utterance": "???????????????????????????"},
            {"utterance": "{AppointmentType}??????????????????"},
        ],
    }
    return utterance_values[language]


def clarification_prompt(language):
    prompt = {
        "English": "I didn't understand you, what would you like me to do?",
        "French": "Je n'ai pas bien compris votre demande, que puis-je faire pour vous?",
        "Italian": "Non ho capito, cosa preferisci che faccia?",
        "Spanish": "No lo entend??, ??qu?? le gustar??a que haga?",
        "German": "Ich habe Sie nicht verstanden. Bitte sagen Sie mir, was ich f??r Sie tun soll.",
        "Japanese": "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????",
    }
    return prompt[language]


def confirmation_prompt(language):
    confirmation_prompt_value = {
        "English": {
            "value": "{Time} is available, should I go ahead and book your appointment?"
        },
        "French": {
            "value": "Je peux prendre rendez-vous ?? {Time}, est-ce que je peux confirmer cette horaire ?"
        },
        "Italian": {
            "value": "L'orario {Time} ?? disponibile. Procedo con la prenotazione dell'appuntamento?"
        },
        "Spanish": {
            "value": "A las {Time} est??n libres, ??quieres que pida la cita para esa hora?"
        },
        "German": {
            "value": "{Time} ist verf??gbar. Soll ich den Termin f??r Sie buchen?"
        },
        "Japanese": {
            "value": "{Time}?????????????????????????????????????????????????????????"
        },
    }
    return confirmation_prompt_value[language]


def decline_reponse(language):
    decline_response_value = {
        "English": {"value": "Okay, I will not schedule an appointment."},
        "French": {"value": "D'accord, je ne confirmerai pas ce rendez-vous."},
        "Italian": {"value": "OK. Non programmer?? un appuntamento."},
        "Spanish": {"value": "Vale, no pedir?? la cita."},
        "German": {"value": "OK, ich werde keinen Termin planen."},
        "Japanese": {"value": "?????????????????????????????????????????????????????????"},
    }
    return decline_response_value[language]


def closing_response(language):
    closing_response_value = {
        "English": {"value": "Done."},
        "French": {"value": "Fini."},
        "Italian": {"value": "Finito."},
        "Spanish": {"value": "Terminado."},
        "German": {"value": "Fertig."},
        "Japanese": {"value": "??????????????????????????????"},
    }
    return closing_response_value[language]


def slot_message(language, slot_type):
    slot_message_values = {
        "English": {
            "appointmentType": {
                "value": "What type of appointment would you like to schedule?"
            },
            "date": {"value": "When should I schedule your appointment?"},
            "time": {"value": "At what time should I schedule your appointment?"},
        },
        "French": {
            "appointmentType": {
                "value": "Quel type de rendez-vous souhaitez-vous prendre ?"
            },
            "date": {"value": "Quand souhaitez-vous prendre rendez-vous ?"},
            "time": {"value": "?? quelle heure souhaitez-vous prendre rendez-vous ?"},
        },
        "Italian": {
            "appointmentType": {
                "value": "Quale tipo di appuntamento vorresti programmare?"
            },
            "date": {"value": "Quando devo programmare il tuo appuntamento?"},
            "time": {"value": "A che ora devo programmare il tuo appuntamento?"},
        },
        "Spanish": {
            "appointmentType": {"value": "??Qu?? tipo de cita quieres pedir?"},
            "date": {"value": "??Para cu??ndo quieres la cita?"},
            "time": {"value": "??Para qu?? hora te pido la cita?"},
        },
        "German": {
            "appointmentType": {"value": "Welchen Typ von Termin m??chten Sie planen?"},
            "date": {"value": "F??r welches Datum soll ich den Termin planen?"},
            "time": {"value": "F??r welche Uhrzeit soll ich den Termin planen?"},
        },
        "Japanese": {
            "appointmentType": {"value": "????????????????????????????????????????????????"},
            "date": {"value": "????????????????????????????????????????????????"},
            "time": {"value": "????????????????????????????????????????????????"},
        },
    }
    return slot_message_values[language][slot_type]
