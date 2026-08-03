import { useState } from "react";

import Header from "../components/Header";
import ResearchForm from "../components/ResearchForm";
import SummaryCard from "../components/SummaryCard";

export default function Dashboard() {

    const [research, setResearch] = useState(null);

    return (
        <div className="container">

            <Header />

            <ResearchForm
                setResearch={setResearch}
            />

            {
                research && (
                    <SummaryCard
                        research={research}
                    />
                )
            }

        </div>
    );
}