import { createStore } from "redux";

const reducer = (state = { messages: [] }, action) => {
  if (action.type === "ADD") {
    return { ...state, messages: [...state.messages, action.payload] };
  }
  return state;
};

export const store = createStore(reducer);