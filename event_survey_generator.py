import pandas as pd 
import json
from datetime import datetime

#### EVENT SURVEY GENERATOR PARAMETERS
survey_name = "Mondavi Center Fall Quarter Events for MCAAC"
survey_file = "{}.qsf".format(survey_name)

events_data = pd.read_excel("Mondavi Center Fall Quarter Events for MCAAC.xlsx", header = None)
events_data.columns = ["event_name", "date", "time", "link"] #, "notes"]
events_data = events_data.loc[(events_data["event_name"].notna()) & (events_data["date"].notna())]

events = list(events_data["event_name"])
dates = list(events_data["date"])
times = list(events_data["time"])
links = list(events_data["link"])
#### END PARAMETERS

num_events = len(events)

survey_id = "SV_9KnnHSHqD3voJ3E"
survey_owner_id = "UR_3WUHDMGK0A1YPvo"
email_q_id = 4

survey_directions = "In this survey, you will select Fall Quarter Mondavi Center events that you are interested in attending, the number of tickets requested, and a ranking prioritizing which events you would most like to attend."
select_question_text = "Select which events you would like to attend by tapping the corresponding boxes. In the text fields of the selected events, enter the number of tickets you would like (<b>1-2 only</b>)."
ranking_question_text = "Rank your selected events in order of preference by dragging the choices to reorder their ranks."

def create_block(block_num, q_ids):
    block = {
        "Type": "Standard",
        "SubType": "",
        "Description": "Block {}".format(block_num),
        "ID": "BL_{}".format(block_num),
        "BlockElements": []
    }

    for q_id in q_ids:
        block["BlockElements"].append({
            "Type": "Question",
            "QuestionID": "QID{}".format(q_id)
        })
    return block

def create_flow(block_num, flow_id):
    flow = {
        "Type": "Standard",
        "ID": "BL_{}".format(block_num),
        "FlowID": "FL_{}".format(flow_id),
        "Autofill": []
    }
    return flow

survey_entry = {
    "SurveyID": survey_id,
    "SurveyName": survey_name,
    "SurveyDescription": None,
    "SurveyOwnerID": survey_owner_id,
    "SurveyBrandID": "ucdavis",
    "DivisionID": "DV_bCz0vLDEYcivdHv",
    "SurveyLanguage": "EN",
    "SurveyActiveResponseSet": "RS_bebPfeTMeXPODAi",
    "SurveyStatus": "Active",
    "SurveyStartDate": "0000-00-00 00:00:00",
    "SurveyExpirationDate": "0000-00-00 00:00:00",
    "SurveyCreationDate": "2022-03-01 08:18:25",
    "CreatorID": survey_owner_id,
    "LastModified": "2022-03-01 22:36:56",
    "LastAccessed": "0000-00-00 00:00:00",
    "LastActivated": "2022-03-01 08:32:49",
    "Deleted": None
}

survey_blocks = {
    "SurveyID": survey_id,
    "Element": "BL",
    "PrimaryAttribute": "Survey Blocks",
    "SecondaryAttribute": None,
    "TertiaryAttribute": None,
    "Payload": {
        "1": {
            "Type": "Trash",
            "Description": "Trash / Unused Questions",
            "ID": "BL_1",
            "BlockElements": []
        }
    }
}
survey_blocks_payload = survey_blocks["Payload"]

survey_flow = {
    "SurveyID": survey_id,
    "Element": "FL",
    "PrimaryAttribute": "Survey Flow",
    "SecondaryAttribute": None,
    "TertiaryAttribute": None,
    "Payload": {
        "Type": "Root",
        "FlowID": "FL_1",
        "Flow": [],
        "Properties": {
            "Count": 10,
            "RemovedFieldsets": []
        }
    }
}
survey_flow_payload = survey_flow["Payload"]

survey_info = [
    {
        "SurveyID": survey_id,
        "Element": "RS",
        "PrimaryAttribute": "RS_bebPfeTMeXPODAi",
        "SecondaryAttribute": None,
        "TertiaryAttribute": None,
        "Payload": None
    },
    {
        "SurveyID": survey_id,
        "Element": "SO",
        "PrimaryAttribute": "Survey Options",
        "SecondaryAttribute": None,
        "TertiaryAttribute": None,
        "Payload": {
            "BackButton": "true",
            "SaveAndContinue": "true",
            "SurveyProtection": "PublicSurvey",
            "BallotBoxStuffingPrevention": "false",
            "NoIndex": "Yes",
            "SecureResponseFiles": "true",
            "SurveyExpiration": "None",
            "SurveyTermination": "DisplayMessage",
            "Header": "",
            "Footer": "",
            "ProgressBarDisplay": "None",
            "PartialData": "+1 week",
            "ValidationMessage": None,
            "PreviousButton": " ← ",
            "NextButton": " → ",
            "SurveyTitle": survey_name,
            "SkinLibrary": "ucdavis",
            "SkinType": "templated",
            "Skin": {
                "brandingId": "*6377849726",
                "templateId": "*base",
                "overrides": {
                    "layout": {
                        "spacing": 0
                    },
                    "questionText": {
                        "size": "18px"
                    },
                    "answerText": {
                        "size": "16px"
                    }
                }
            },
            "NewScoring": 1,
            "EOSMessage": "MS_bPDI4TK7DI3ICJo",
            "ShowExportTags": "false",
            "CollectGeoLocation": "false",
            "SurveyMetaDescription": "The most powerful, simple and trusted way to gather experience data. Start your journey to experience management and try a free account today.",
            "PasswordProtection": "No",
            "AnonymizeResponse": "No",
            "RefererCheck": "No",
            "UseCustomSurveyLinkCompletedMessage": None,
            "SurveyLinkCompletedMessage": None,
            "SurveyLinkCompletedMessageLibrary": None,
            "ResponseSummary": "No",
            "EOSMessageLibrary": survey_owner_id,
            "EOSRedirectURL": "http://",
            "EmailThankYou": "false",
            "ThankYouEmailMessageLibrary": None,
            "ThankYouEmailMessage": None,
            "ValidateMessage": "false",
            "ValidationMessageLibrary": None,
            "InactiveSurvey": "DefaultMessage",
            "PartialDeletion": None,
            "PartialDataCloseAfter": "LastActivity",
            "InactiveMessageLibrary": None,
            "InactiveMessage": None,
            "AvailableLanguages": {
                "EN": []
            },
            "ProtectSelectionIds": True,
            "CustomStyles": [],
            "SurveyName": survey_name
        }
    },
    {
      "SurveyID": survey_id,
      "Element": "TR",
      "PrimaryAttribute": "TR_elXawPjSoXqEGmG",
      "SecondaryAttribute": None,
      "TertiaryAttribute": None,
      "Payload": {
        "TriggerAction": "EmailMessage",
        "Type": "OnSurveyComplete",
        "ToEmail": "${q://QID4/ChoiceTextEntryValue}",
        "FromName": "lbha@ucdavis.edu",
        "FromEmail": "lbha@ucdavis.edu",
        "SendDate": "now",
        "Subject": "[MCAAC] Mondavi Center Fall Quarter Events for MCAAC Responses",
        "Message": "<p>Dear ${q://QID3/ChoiceTextEntryValue},</p>\nThank you for filling out the Mondavi Center Fall Quarter Events Survey! A summary of your responses is below.<br />\n<br />\nBest,<br />\nMCAAC Ticket Allocations Committee",
        "IncludeReport": True,
        "UseFullText": True,
        "ID": "TR_elXawPjSoXqEGmG"
      }
    },
    {
        "SurveyID": survey_id,
        "Element": "SCO",
        "PrimaryAttribute": "Scoring",
        "SecondaryAttribute": None,
        "TertiaryAttribute": None,
        "Payload": {
            "ScoringCategories": [],
            "ScoringCategoryGroups": [],
            "ScoringSummaryCategory": None,
            "ScoringSummaryAfterQuestions": 0,
            "ScoringSummaryAfterSurvey": 0,
            "DefaultScoringCategory": None,
            "AutoScoringCategory": None
        }
    },
    {
        "SurveyID": survey_id,
        "Element": "PROJ",
        "PrimaryAttribute": "CORE",
        "SecondaryAttribute": None,
        "TertiaryAttribute": "1.1.0",
        "Payload": {
            "ProjectCategory": "CORE",
            "SchemaVersion": "1.1.0"
        }
    },
    {
        "SurveyID": survey_id,
        "Element": "STAT",
        "PrimaryAttribute": "Survey Statistics",
        "SecondaryAttribute": None,
        "TertiaryAttribute": None,
        "Payload": {
            "MobileCompatible": True,
            "ID": "Survey Statistics"
        }
    },
    {
        "SurveyID": "SV_9KnnHSHqD3voJ3E",
        "Element": "QC",
        "PrimaryAttribute": "Survey Question Count",
        "SecondaryAttribute": "10",
        "TertiaryAttribute": None,
        "Payload": None
    },
]

survey_elements = [
    survey_blocks,
    survey_flow
] + survey_info

survey_json = {
    "SurveyEntry": survey_entry,
    "SurveyElements": survey_elements,
}

# QUESTIONS
question_count = 0
block_num = 2
flow_num = 2

pg1_description = {
    "SurveyID": survey_id,
    "Element": "SQ",
    "PrimaryAttribute": "QID{}".format(question_count),
    "SecondaryAttribute": "{}".format(survey_directions),
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": "<h4>{}</h4>".format(survey_directions),
        "DefaultChoices": False,
        "DataExportTag": "Q{}".format(question_count),
        "QuestionType": "DB",
        "Selector": "TB",
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "{}".format(survey_directions),
        "ChoiceOrder": [],
        "Validation": {
            "Settings": {
                "Type": "None"
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 4,
        "NextAnswerId": 1,
        "QuestionID": "QID{}".format(question_count)
    }
}
survey_elements.append(pg1_description)

question_count += 1

event_select_question = {
    "SurveyID": survey_id,
    "Element": "SQ",
    "PrimaryAttribute": "QID{}".format(question_count),
    "SecondaryAttribute": "{}".format(select_question_text),
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": "{}".format(select_question_text),
        "DefaultChoices": False,
        "DataExportTag": "Q{}".format(question_count),
        "QuestionType": "MC",
        "Selector": "MACOL",
        "Configuration": {
            "QuestionDescriptionOption": "UseText",
            "NumColumns": 2
        },
        "QuestionDescription": "{}".format(select_question_text),
        "Choices": {},
        "ChoiceOrder": list(range(1, num_events + 1)),
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "MinChoices",
                "MinChoices": "1",
                "MaxChoices": str(num_events),
                "CustomValidation": None
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": num_events + 1,
        "NextAnswerId": 1,
        "QuestionID": "QID{}".format(question_count),
        "DataVisibility": {
            "Private": False,
            "Hidden": False
        },
        "DynamicChoicesData": [],
        "SubSelector": "TX"
    }
}

for i in range(1, num_events + 1):
    formatted_date = dates[i - 1].strftime("%-m/%d/%Y")
    formatted_time = times[i - 1].strftime("%-I:%M %p")
    event_display = "<center><a href = '{}' target = '_blank'>{}</a><br><br> {} | {} </center>".format(links[i - 1], events[i - 1], formatted_date, formatted_time)
    event_select_question["Payload"]["Choices"][i] = {
        "Display": event_display,
        "TextEntry": "true",
        "TextEntryValidation": "ValidNumber",
        "TextEntryForceResponse": True
    }

survey_elements.append(event_select_question)

pg1_q_ids = range(question_count + 1)
survey_blocks_payload[block_num] = create_block(block_num, pg1_q_ids)
survey_flow_payload["Flow"].append(create_flow(block_num, flow_num))

selected_qid = question_count
question_count += 1
block_num += 1
flow_num += 1

ranking_question = {
    "SurveyID": survey_id,
    "Element": "SQ",
    "PrimaryAttribute": "QID{}".format(question_count),
    "SecondaryAttribute": "{}".format(ranking_question_text),
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": "{}".format(ranking_question_text),
        "DefaultChoices": {},
        "DataExportTag": "Q{}".format(question_count),
        "QuestionType": "RO",
        "Selector": "DND",
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "{}".format(ranking_question_text),
        "Choices": [],
        "ChoiceOrder": [],
        "Validation": {
            "Settings": {
                "ForceResponse": "ON"
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 1,
        "NextAnswerId": 1,
        "QuestionID": "QID{}".format(question_count),
        "DynamicChoices": {
            "DynamicType": "ChoiceGroup",
            "Locator": "q://QID{}/ChoiceGroup/SelectedChoices".format(selected_qid),
            "Type": "Dynamic"
        },
        "DynamicChoicesData": [],
        "DataVisibility": {
            "Private": False,
            "Hidden": False
        },
        "SubSelector": "TX",
        "QuestionJS": "Qualtrics.SurveyEngine.addOnload(function()\n{\n\t/*Place your JavaScript here to run when the page loads*/\n\n});\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\tjQuery(\"#\"+this.questionId+\" .InputText\").hide();\n\n});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});"
    }
}

for i in range(1, num_events + 1):
    ranking_question["Payload"]["DefaultChoices"]["x{}".format(i)] = {
        "Text": "${q://QID" + str(selected_qid) + "/ChoiceTextEntryValue/" + str(i) + "}",
        "Value": str(i)
    }

survey_elements.append(ranking_question)

pg2_q_ids = [question_count]
survey_blocks_payload[block_num] = create_block(block_num, pg2_q_ids)
survey_flow_payload["Flow"].append(create_flow(block_num, flow_num))

question_count += 1
block_num += 1
flow_num += 1

name_question = {
    "SurveyID": survey_id,
    "Element": "SQ",
    "PrimaryAttribute": "QID{}".format(question_count),
    "SecondaryAttribute": "Name",
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": "<h4>Name</h4>",
        "DefaultChoices": False,
        "DataExportTag": "Q{}".format(question_count),
        "QuestionType": "TE",
        "Selector": "SL",
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "Name",
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None"
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 4,
        "NextAnswerId": 1,
        "SearchSource": {
            "AllowFreeResponse": "false"
        },
        "QuestionID": "QID{}".format(question_count)
    }
}
survey_elements.append(name_question)

question_count += 1

email_question = {
    "SurveyID": survey_id,
    "Element": "SQ",
    "PrimaryAttribute": "QID{}".format(question_count),
    "SecondaryAttribute": "Email",
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": "<h4>Email</h4>",
        "DefaultChoices": False,
        "DataExportTag": "Q{}".format(question_count),
        "QuestionType": "TE",
        "Selector": "SL",
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "Email",
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "ContentType",
                "MinChars": "1",
                "ContentType": "ValidEmail",
                "ValidDateType": "DateWithFormat",
                "ValidPhoneType": "ValidUSPhone",
                "ValidZipType": "ValidUSZip",
                "ValidNumber": {
                    "Min": "",
                    "Max": "",
                    "NumDecimals": ""
                }
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 4,
        "NextAnswerId": 1,
        "SearchSource": {
            "AllowFreeResponse": "false"
        },
        "QuestionID": "QID{}".format(question_count)
    }
}
survey_elements.append(email_question)

question_count += 1

accessibility_question = {
    "SurveyID": survey_id,
    "Element": "SQ",
    "PrimaryAttribute": "QID{}".format(question_count),
    "SecondaryAttribute": "Accessibility Needs",
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": "<h4>Accessibility Needs</h4>",
        "DefaultChoices": False,
        "DataExportTag": "Q{}".format(question_count),
        "QuestionType": "TE",
        "Selector": "SL",
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "Accessibility Needs",
        "Validation": {
            "Settings": {
                "ForceResponse": "OFF",
                "ForceResponseType": "OFF",
                "Type": "None"
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 4,
        "NextAnswerId": 1,
        "SearchSource": {
            "AllowFreeResponse": "false"
        },
        "QuestionID": "QID{}".format(question_count)
    }
}
survey_elements.append(accessibility_question)

pg1_q_ids = range(3, question_count + 1)
survey_blocks_payload[block_num] = create_block(block_num, pg1_q_ids)
survey_flow_payload["Flow"].append(create_flow(block_num, flow_num))

with open(survey_file, "w") as f:
    json.dump(survey_json, f, ensure_ascii = True, indent = 4)
