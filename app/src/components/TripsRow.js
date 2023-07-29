export default function TripRow({trip, removeTrip}) {
    return (
        <tr>
            <td>{trip.name}</td>
            <td>{trip.start_date}</td>
            <td>{trip.end_date}</td>
            <td>{trip.organizer}</td>
        </tr>
    )
}