import url from '../api.json'
import { useState } from 'react';

export default function CreateAccountPage() {
    const [accountData, setAccountData] = useState({
        email: "",
        password: "",
        first_name: "",
        last_name: ""
    });

    const handleFormChange = (event) => {
        const { name, value} = event.target;
        setAccountData((prevAccountData) => ({
            ...prevAccountData,
            [name]: value
        }));
    }

    const handleCreateAccount = (event) => {
        console.log(accountData);
    }

    return (
        <form onSubmit={handleCreateAccount}>
            <h3>Create Account</h3>
            <input type="text" name="first_name" placeholder="First Name" value={accountData.first_name} onChange={handleFormChange} required />
            <br />
            <input type="text" name="last_name" placeholder="Last Name" value={accountData.last_name} onChange={handleFormChange} required />
            <br />
            <input type="text" name="email" placeholder="Email" value={accountData.email} onChange={handleFormChange} required />
            <br />
            <input type="text" name="password" placeholder="Password" value={accountData.password} onChange={handleFormChange} required />
            <br />
            <button type="submit">Create Account</button>
        </form>
    )
}