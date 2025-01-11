# tributary

The sensor streaming system's backend infrastructure for Ford. This project includes a Flask server that exposes two APIs and records data to a Redis database. Embedded sensors in a car periodically access the /record endpoint to upload data to the database. A user-facing mobile application then uses the /collect endpoint to retrieve the data.
