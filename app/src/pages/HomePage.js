import url from '../api.json'
import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TripsTable from '../components/TripsTable';

export default function Homepage() {
    const [user, setUser] = useState([]);
    const [greeting, setGreeting] = useState([]);
    const [trips, setTrips] = useState([]);

    const loadUserInfo = async () => {
        const user_response = await fetch(url['url'] + `/user/1`);
        const user = await user_response.json();
        setUser(user);

        const trips_response = await fetch(url['url'] + `/mytrips/${user.user_id}`);
        const trips = await trips_response.json();
        setTrips(trips);

        let greeting = "";
        if (user != undefined) {
            greeting = ", " + user.first_name;
        }
        setGreeting(greeting)
    }

    const removeTrip = async trip_id => {
        const response = await fetch(`http://localhost:5000/trips/${trip_id}`, {method: 'DELETE'})
        if (response.status === 204) {
            loadUserInfo();
            alert('Trip deleted successfully.');
        } else {
            console.error(`Failed to delete the trip with id = ${trip_id}, status code = ${response.status}`)
        }
    }

    useEffect(() => {
        loadUserInfo();
    }, []);


    return (
        <div>
            <h1>TriPlanner</h1>
            <h2>Welcome{greeting}</h2>
            <TripsTable trips={trips} removeTrip={removeTrip}/>
        </div>
  )
}