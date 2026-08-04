import { useState } from "react";
import { createResearch } from "../services/api";
import Notification from "./Notification";

export default function ResearchForm({
    setResearch,
    loading,
    setLoading
}) {

    const [topic, setTopic] = useState("");

    const [notification, setNotification] = useState({
        type: "",
        message: ""
    });

    const handleResearch = async () => {

        if (!topic.trim()) return;

        setLoading(true);

        try {

            const result = await createResearch(topic);

            setResearch(result);

            setTopic("");

            setNotification({
                type: "success",
                message: "Research completed successfully."
            });

        } catch (error) {

            console.error("Research failed:", error);

            setNotification({
                type: "error",
                message: "Failed to generate research. Please try again."
            });

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="research-card">

            <h2>Research Topic</h2>

            <div className="research-form">

                <input
                    type="text"
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    placeholder="Artificial Intelligence in Banking"
                    disabled={loading}
                />

                <button
                    onClick={handleResearch}
                    disabled={loading || !topic.trim()}
                >
                    {loading ? "Researching..." : "Start Research"}
                </button>

            </div>

            <Notification
                type={notification.type}
                message={notification.message}
                onClose={() =>
                    setNotification({
                        type: "",
                        message: ""
                    })
                }
            />

        </div>

    );

}