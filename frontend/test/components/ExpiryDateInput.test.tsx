import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { userEvent } from "@testing-library/user-event";
import ExpiryDateInput from "@/components/ExpiryDateInput";

describe("Render", () => {
  it("Should have a label", () => {
    render(<ExpiryDateInput />);
    const label = screen.getByTestId("dateLabel");
    expect(label).toBeInTheDocument();
  });
  it("Should have a span text in the label", () => {
    render(<ExpiryDateInput />);
    const span = screen.getByText("When should it expire naturally?");
    expect(span).toBeInTheDocument();
  });
  it("Should have a datetime input field", () => {
    render(<ExpiryDateInput />);
    const input = screen.getByTestId("datetime-input");
    expect(input).toBeInTheDocument();
  });
  it("Should have a placeholder", () => {
    render(<ExpiryDateInput />);
    const input = screen.getByTestId("datetime-input");
    expect(input).toBeInTheDocument();
});
it("Should have an input that is required", ()=>{
    render(<ExpiryDateInput />)
    const input = screen.getByTestId("datetime-input");
    expect(input).toBeRequired()
  })
  it("Should have an input that only accepts positive numbers", ()=>{
    render(<ExpiryDateInput />)
    const input : HTMLInputElement = screen.getByTestId("datetime-input");
    const minAttr = parseInt(input.getAttribute("min") || "")
    expect(minAttr).toBe(1)
  })
});
describe("Behavior", () => {
  const mockHandleChange = jest.fn();
  it("Should be able to add date to date", async () => {
    render(<ExpiryDateInput handleChange={mockHandleChange} />);
    const input : HTMLInputElement = screen.getByTestId("datetime-input");
    await userEvent.type(input, "2022-01-01T12:00");
    expect(mockHandleChange).toHaveBeenCalled();
    expect(input.value).toBe("2022-01-01T12:00")
  });
});
