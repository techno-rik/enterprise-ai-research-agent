import {
    CircleCheck,
    Globe,
    Bot,
    Database
} from "lucide-react";

export default function StatsBar({ research }) {

    return (

        <div className="stats-grid">

            <div className="stat-card">

                <CircleCheck size={28} />

                <div>

                    <h4>Status</h4>

                    <p>{research.status}</p>

                </div>

            </div>

            <div className="stat-card">

                <Globe size={28} />

                <div>

                    <h4>Sources</h4>

                    <p>{research.sources_found ?? 0}</p>

                </div>

            </div>

            <div className="stat-card">

                <Bot size={28} />

                <div>

                    <h4>AI Model</h4>

                    <p>Llama 3.3</p>

                </div>

            </div>

            <div className="stat-card">

                <Database size={28} />

                <div>

                    <h4>Vector DB</h4>

                    <p>ChromaDB</p>

                </div>

            </div>

        </div>

    );

}