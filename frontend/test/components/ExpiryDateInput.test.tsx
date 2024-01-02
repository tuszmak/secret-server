import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
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
});
