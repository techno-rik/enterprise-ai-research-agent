import { useState } from "react";

import Header from "../components/Header";
import ResearchForm from "../components/ResearchForm";
import SummaryCard from "../components/SummaryCard";
import ChatPanel from "../components/ChatPanel";
import LoadingOverlay from "../components/LoadingOverlay";
import StatsBar from "../components/StatsBar";
import WelcomeCard from "../components/WelcomeCard";

export default function Dashboard() {

    const [research, setResearch] = useState(null);
    const [loading, setLoading] = useState(false);

    return (
        <div className="container">

            <Header />

            <ResearchForm
            setResearch={setResearch}
            loading={loading}
            setLoading={setLoading}
            />

            {!research && <WelcomeCard />}

            {research && (
    <>
        <StatsBar research={research} />

        <SummaryCard
            research={research}
        />
    </>
)}

            {research && (
                <ChatPanel />
            )}

            {loading && <LoadingOverlay />}
        </div>
    );
}