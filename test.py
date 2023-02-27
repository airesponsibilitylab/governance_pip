# example.py
import governance

results = governance.Results()
results.set_api_key("<YOUR MISSION CONTROL API KEY>")
results.set_server_url("<THE BASE URL FOR YOUR MISSION CONTROL DEPLOYMENT>")
results.set_agent_id("<YOUR MISSION CONTROL AGENT ID>")
results.set_project_id("<YOUR MISSION CONTROL PROJECT ID>")
results.set_stage_id("<YOUR MISSION CONTROL STAGE ID>")
results.set_agent_token("<YOUR MISSION CONTROL TOKEN>")

# Some amount of data science work is done
results.submit({"key1": "value1", "key2": "value2"})