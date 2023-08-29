class Flight:
    def __init__(self, flight_id, source, destination, departure_time, arrival_time):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

class FlightDatabase:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source):
        results = []
        for flight in self.flights:
            if flight.source == source:
                results.append(flight)
        return results

    def search_by_destination(self, destination):
        results = []
        for flight in self.flights:
            if flight.destination == destination:
                results.append(flight)
        return results

def main():
    database = FlightDatabase()

    # Populate the database with flight details (you can add more flights)
    database.add_flight(Flight("F101", "New York", "Los Angeles", "08:00", "12:00"))
    database.add_flight(Flight("F102", "Los Angeles", "Chicago", "10:00", "14:00"))
    # Add more flights here...

    user_input = int(input("Enter 1 to search by Flight ID, 2 to search by source city, 3 to search by destination city: "))

    if user_input == 1:
        flight_id = input("Enter Flight ID: ")
        flight = database.search_by_id(flight_id)
        if flight:
            print("Flight Details:")
            print(f"Flight ID: {flight.flight_id}")
            print(f"Source: {flight.source}")
            print(f"Destination: {flight.destination}")
            print(f"Departure Time: {flight.departure_time}")
            print(f"Arrival Time: {flight.arrival_time}")
        else:
            print("Flight not found.")

    elif user_input == 2:
        source_city = input("Enter Source City: ")
        results = database.search_by_source(source_city)
        if results:
            print("Flights from", source_city)
            for flight in results:
                print(f"Flight ID: {flight.flight_id}, Destination: {flight.destination}")
        else:
            print("No flights found from", source_city)

    elif user_input == 3:
        dest_city = input("Enter Destination City: ")
        results = database.search_by_destination(dest_city)
        if results:
            print("Flights to", dest_city)
            for flight in results:
                print(f"Flight ID: {flight.flight_id}, Source: {flight.source}")
        else:
            print("No flights found to", dest_city)

    else:
        print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
