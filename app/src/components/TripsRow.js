export default function TripRow({trip, removeTrip}) {
    return (
        <tr>
            <td>{trip[0]}</td>
            <td>{trip[1]}</td>
            <td>{trip[2]}</td>
            <td>{trip[3]}</td>
        </tr>
    )
}