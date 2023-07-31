import url from '../api.json'
import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TripsTable from '../components/TripsTable';

export default function Homepage() {
    const [user, setUser] = useState([]);
    const [trips, setTrips] = useState([]);

    const loadUser = async () => {
        const response = await fetch(url['url'] + `/user/1`);
        const user = await response.json();
        console.log(user);
        setUser(user);
    }

    const loadTrips = async () => {
        const response = await fetch(url['url'] + `/mytrips/${user.user_id}`);
        const trips = await response.json();
        setTrips(trips);
    }

    const removeTrip = async trip_id => {
        const response = await fetch(`http://localhost:5000/trips/${trip_id}`, {method: 'DELETE'})
        if (response.status === 204) {
            loadTrips();
            alert('Trip deleted successfully.');
        } else {
            console.error(`Failed to delete the trip with id = ${trip_id}, status code = ${response.status}`)
        }
    }

    useEffect(() => {
        loadTrips();
        loadUser();
    }, []);

    return (
        <div>
            <h1>TriPlanner</h1>
            <h2>Welcome{", " + user.first_name}</h2>
            <TripsTable trips={trips} removeTrip={removeTrip}/>
        </div>
  )
}