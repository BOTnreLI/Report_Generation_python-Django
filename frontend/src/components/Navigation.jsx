import {Link, useNavigate} from "react-router-dom"

function Navigation({ onLogout }) {
    const navigate = useNavigate();

    const handleLogout = () => {
        onLogout();
        navigate("/")
    }

};

export default Navigation