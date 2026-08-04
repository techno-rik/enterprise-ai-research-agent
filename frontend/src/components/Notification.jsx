import { CheckCircle, AlertCircle, X } from "lucide-react";

export default function Notification({
    type = "success",
    message,
    onClose
}) {

    if (!message) return null;

    return (

        <div className={`notification ${type}`}>

            <div className="notification-content">

                {
                    type === "success"
                        ? <CheckCircle size={20}/>
                        : <AlertCircle size={20}/>
                }

                <span>{message}</span>

            </div>

            <button
                className="notification-close"
                onClick={onClose}
            >
                <X size={18}/>
            </button>

        </div>

    );

}