import { Link2 } from "lucide-react";

export default function SourcesCard({ research }) {

    return (

        <div className="research-card">

            <h2
                style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "10px"
                }}
            >
                <Link2 size={22} />

                Sources Used ({research.sources_found})
            </h2>

            <ul className="info-list">

                {research.sources.map((source, index) => (

                    <li key={index}>

                        <a
                            href={source.url}
                            target="_blank"
                            rel="noreferrer"
                            className="source-link"
                        >
                            {source.title}
                        </a>

                    </li>

                ))}

            </ul>

        </div>

    );

}