import InfoCard from "./InfoCard";
import SourcesCard from "./SourcesCard";
import { FileText } from "lucide-react";

export default function SummaryCard({ research }) {

    const summary = research.summary;

    return (
        <>

            {/* Executive Summary */}

            <div className="research-card">

                <h2
    style={{
        display:"flex",
        alignItems:"center",
        gap:"10px"
    }}
>

    <FileText size={22}/>

    Executive Summary

</h2>

                <p
                    style={{
                        marginTop: "20px",
                        lineHeight: "1.8"
                    }}
                >
                    {summary.executive_summary}
                </p>

            </div>

            {/* Findings + Risks */}

            <div className="grid">

                <InfoCard
                    title="Key Findings"
                    items={summary.key_findings}
                />

                <InfoCard
                    title="Risks"
                    items={summary.risks}
                />

            </div>

            {/* Opportunities */}

            <InfoCard
                title="Opportunities"
                items={summary.opportunities}
            />

            {/* Sources */}

            <SourcesCard
    research={research}
/>

        </>
    );

}