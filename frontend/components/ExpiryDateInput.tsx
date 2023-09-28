import React from 'react'

function ExpiryDateInput({handleChange}:any) {
  return (
    <div className="form-control w-full max-w-xs">
      <label className="label">
        <span className="label-text text-xl">When should it expire naturally?</span>
      </label>
      <input
        type="datetime-local"
        placeholder="Type here"
        className="input input-bordered w-full max-w-xs"
        onChange={handleChange}
        min={1}
        required
      />
    </div>
  )
}

export default ExpiryDateInput