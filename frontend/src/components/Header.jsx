import { Brain, Activity } from "lucide-react";

export default function Header() {

    return (

        <div className="header">

            <div>

                <h1 className="header-title">

                    <Brain size={38} />

                    <span>InsightForge AI</span>

                </h1>

                <p className="subtitle">
                    Enterprise Research Intelligence Platform
                </p>

            </div>

            <div className="status-badge">

                <Activity size={16} />

                <span>Online</span>

            </div>

        </div>

    );

}