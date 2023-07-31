import TripsRow from './TripsRow';

export default function TripsTable({trips, removeTrip}) {
    return (
        <div>
            <table>
                <caption>My Trips</caption>
                <thead>
                    <tr>
                        <th>Trip</th>
                        <th>From</th>
                        <th>To</th>
                        <th>Organizer</th>
                    </tr>
                </thead>
                <tbody>
                    {trips.map((trip, i) => <TripsRow trip={trip} removeTrip={removeTrip} key={i} />)}
                </tbody>
            </table>
        </div>
    )
}