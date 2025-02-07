import React from "react";

export const Interactive = ({params, setParams}) => (
    <div className="space-y-2">
        {Object.keys(params).map(key => (
            <div key={key}>
                <label>{key}: </label>
                <input
                    type="number"
                    step="0.1"
                    value={params[key]}
                    onChange={(e) => setParams(prev => ({
                        ...prev,
                        [key]: Number(e.target.value)
                    }))}
                />
            </div>
        ))}
    </div>
)