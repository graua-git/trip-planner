
-- MyTrips Query
SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS trip, owner
FROM Memberships
JOIN Users ON Users.user_id = Memberships.user
JOIN Trips on Trips.trip_id = Memberships.trip

SELECT name, start_date, end_date, organizer
FROM Trips
JOIN Memberships ON Memberships.trip = Trips.trip_id
JOIN Users ON Users.user_id = Memberships.user
JOIN (SELECT trip, owner, CONCAT(Users.first_name, ' ', Users.last_name) as organizer
FROM Memberships
JOIN Users ON Users.user_id = Memberships.user
WHERE owner = 1) as Owners ON  Trips.trip_id = Owners.trip
WHERE Users.user_id = {}