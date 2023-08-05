import url from '../api.json'
import { useState } from 'react';

export default function Homepage() {
    const [formData, setFormData] = useState({
        email: "",
        password: ""
    });

    const handleFormChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value,
        }));
    }

    const handleLogin = (event) => {
        event.preventDefault();
        console.log(formData);
        console.log(JSON.stringify(formData));
        fetch(url['url'] + `/login`, {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(formData)})
            .then((response) => response.json())
            .then((data) => {
                console.log("Login Successful:", data);
            })
            .catch((error) => {
                console.error("Error during login:", error);
            });
    }

    return (
        <form onSubmit={handleLogin}>
            <h3>Login</h3>
            <label for="email">Email: </label>
            <br />
            <input type="text" name="email" placeholder="email" value={formData.email} onChange={handleFormChange} required />
            <br />
            <label for="password">Password: </label>
            <br />
            <input type="text" name="password" placeholder="password" value={formData.password} onChange={handleFormChange} required />
            <br />
            <button type="submit">Login</button>

        </form>
    )
}