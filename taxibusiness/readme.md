In this practice you need to accomplish the following:

Create a model called TaxiBusiness.
In TaxiBusiness it should have the following fields:
 'Occupied' a boolean stating if it's occupied or not.
 'Capacity' an integer stating how many passengers can sit in the taxi
 'Number of Passengers' an integer stating the current number of passengers
 'Fare' a float stating the cost per mile for travel for that taxi.
 'Taxi-Type' a string detailing the type of taxi (Van, Car, Bus).
 'Taxi-Number' an integer stating the taxi number. This should start at 111 and increase by 11 each other instance of the taxi.
 'Notes' an optional string field for any extra notations.
You should have the following functions capable in your model:
 Create a Taxi.
 Send the Taxi Out on a Fare - should change the number of passengers (cannot be greater than capacity) and occupied boolean to True.
 Finish a fare (should return a cost and take in a distance) and convert the number of passengers to 0 and the occupied boolean to False.
 Remove a Taxi from the system (Delete a taxi model)
 Find a Taxi - Search by Taxi Number to get a specific taxi.
 Filter un-occupied taxis - Filter by occupied status
 Filter by un-occupied and by capacity (over given number and is unoccupied)
You should write your own tests for each of these functionalities.