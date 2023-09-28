import React from 'react'

function NumberInput({handleChange} : any) {
  return (
    <div className="form-control w-full max-w-xs">
      <label className="label">
        <span className="label-text text-xl">How many visits do you allow?</span>
      </label>
      <input
        type="number"
        placeholder="Type here"
        className="input input-bordered w-full max-w-xs"
        onChange={handleChange}
        min={1}
        required
      />
    </div>
  )
}

export default NumberInput