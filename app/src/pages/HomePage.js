import url from '../api.json'
import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TripsTable from '../components/TripsTable';

export default function Homepage() {

    const [trips, setTrips] = useState([]);

    const loadTrips = async () => {
        const response = await fetch(url['url'] + '/mytrips/1');
        const trips = await response.json();
        // const trips = [["Doe Trip","2023-08-05","2023-08-12","John Doe"],["John Trip","2021-06-24","2021-07-02","John Doe"]]
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
    }, []);

    return (
        <div>
            <h1>TriPlanner</h1>
            <h2>Welcome</h2>
            <TripsTable trips={trips} removeTrip={removeTrip}/>
        </div>
  )
}