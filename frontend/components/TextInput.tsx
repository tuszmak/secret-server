import React from "react";

function TextInput({handleChange} : any) {
  return (
    <div className="form-control w-full max-w-xs">
      <label className="label">
        <span className="label-text text-xl">What is your secret?</span>
      </label>
      <input
        type="text"
        placeholder="Type your secret here"
        className="input input-bordered w-full max-w-xs"
        onChange={handleChange}
        required
      />
    </div>
  );
}

export default TextInput;
