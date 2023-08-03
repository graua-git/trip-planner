import { useState } from 'react';

export default function Homepage() {
    const [formData, setFormData] = useState({
        email: "",
        password: ""
    });

    const handleValueChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value,
        }));
    }

    const login = (event) => {
        event.preventDefault();
        console.log(formData.email, formData.password);
    }

    return (
        <form onSubmit={login}>
            <h3>Login</h3>
            <label for="email">Email: </label>
            <br />
            <input type="text" name="email" placeholder="email" value={formData.email} onChange={handleValueChange} required />
            <br />
            <label for="password">Password: </label>
            <br />
            <input type="text" name="password" placeholder="password" value={formData.password} onChange={handleValueChange} required />
            <br />
            <button type="submit">Login</button>

        </form>
    )
}