from models.olive_readings import OliveReadingsManager

# Example usage:
if __name__ == "__main__":
    manager = OliveReadingsManager()

    # Create a new reading
    for i in range(1,6):
        manager.create_reading(sample_time='2023-10-09 12:00:00', nm_525_ON=100*i, nm_525_OFF=200*i,
                            nm_680_ON=300*i, nm_680_OFF=400*i, nm_740_ON=500*i, nm_740_OFF=600*i,
                            nm_980_ON=700*i, nm_980_OFF=800*i, nm_1450_ON=900*i, nm_1450_OFF=1000*i)
    # Retrieve all readings
    readings = manager.get_readings()
    for reading in readings:
        print(f"ID:{reading.id} Sample Time: {reading.sampleTime}, nm_525_ON: {reading.nm_525_ON}, nm_525_OFF: {reading.nm_525_OFF}")

    # Update a reading (provide the ID of the reading to update)
    manager.update_reading(reading_id=2, sample_time='2023-10-10 14:00:00', nm_525_ON=110, nm_525_OFF=220,
                           nm_680_ON=330, nm_680_OFF=440, nm_740_ON=550, nm_740_OFF=660,
                           nm_980_ON=770, nm_980_OFF=880, nm_1450_ON=990, nm_1450_OFF=1111)

    # Delete a reading (provide the ID of the reading to delete)
    manager.delete_reading(1)