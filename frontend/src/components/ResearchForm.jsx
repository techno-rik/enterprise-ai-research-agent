import { useState } from "react";
import { createResearch } from "../services/api";

export default function ResearchForm({ setResearch }) {

    const [topic, setTopic] = useState("");

    const handleResearch = async () => {

        if (!topic.trim()) return;

        const result = await createResearch(topic);

       setResearch(result);
    };

    return (

        <div className="research-card">

            <h2>Research Topic</h2>

            <div className="research-form">

                <input
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    placeholder="Artificial Intelligence in Banking"
                />

                <button onClick={handleResearch}>
                    Start Research
                </button>

            </div>

        </div>

    );
}