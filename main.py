from fastapi import FastAPI
from pydantic import BaseModel

class Sensor(BaseModel):
    sensor_id : str
    temp_c : float
    status : int

class SensorUpdate(BaseModel):
    temp_c : float
    status : int

app = FastAPI()

sensor_data = [
    {"sensor_id": "A1", "temp_c": 45.0, "status": 0},
    {"sensor_id": "A2", "temp_c": 82.5, "status": 2},
    {"sensor_id": "A3", "temp_c": 0.0, "status": 3},  
    {"sensor_id": "A4", "temp_c": 46.1, "status": 0},
    {"sensor_id": "A5", "temp_c": -99.0, "status": 3} 
]

def logging(func):
    def wrapper():
        print("Processing...")
        
        result = func() 
        
        print("Processing Completed Sucessfully. Here are the global statistics.")
        
        return result 

    return wrapper
        
def filter_sensors_by_status(target_status:int):
    target_status_list = []
    for event in sensor_data:
        if event["status"] == target_status:
            target_status_list.append(event)
    
    return target_status_list

def update_sensor_status(target_id:str, new_data:dict):
    for event in sensor_data:
        if target_id == event["sensor_id"]:
            event["temp_c"] = new_data["temp_c"]
            event["status"] = new_data["status"]
    print(f"Updated sensor data for sensor data with id {target_id}")
    return sensor_data

def delete_sensor(target_id:str):
    updated_data = []
    for event in sensor_data:
        if target_id != event["sensor_id"]:
            updated_data.append(event)
    
    return updated_data

@logging
def calculate_global_stats():
    # The total count of broken sensors (status 3).
    # The average temperature of only the working sensors (status 0, 1, or 2).
    count = 0
    total = 0.0
    count_safe = 0
    avg = 0
    for event in sensor_data:
        if event["status"] == 3:
            count+=1
    
    for event in sensor_data:
        if event["status"] !=3:
            total += event["temp_c"]
            count_safe +=1
        avg = float(total/count_safe)
    
    response = {
        "broken_sensors" : count,
        "avg_working_temp" : avg
    }

    return response

@app.get("/")
async def read_root():
    return {"message": "Welcome to the EnviroTech API!"}

@app.get("/sensors")
async def get_all_sensors():
    return {"data": sensor_data}

@app.post("/add_sensor")
async def add_sensor(new_sensor:Sensor):
    sensor_data.append(new_sensor.model_dump())

@app.get("/sensor/filter")
async def filter_data(status:int):
    target_status_list = filter_sensors_by_status(status)
    return target_status_list

@app.put("/sensor/update")
async def update_data(target_id:str, new_data:SensorUpdate):
    updated_list = update_sensor_status(target_id, new_data.model_dump())
    return updated_list

@app.delete("/sensor/delete_sensor")
async def deleted_sensor(target_id:str):
    global sensor_data
    sensor_data = delete_sensor(target_id)
    return sensor_data

@app.get("/sensor/global_stats")
async def global_stats():
    global_stats = calculate_global_stats()
    return global_stats

    
