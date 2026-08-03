export default function SummaryCard({ research }) {

    const summary = research.summary;

    return (

        <div className="research-card">

            <h2>Executive Summary</h2>

            <p
                style={{
                    marginTop: "20px",
                    lineHeight: "1.8"
                }}
            >
                {summary.executive_summary}
            </p>

        </div>

    );
}