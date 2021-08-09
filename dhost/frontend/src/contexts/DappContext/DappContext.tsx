
import { SetStateAction, Dispatch } from "react";
import { createContext, FC, Context, useState, useContext } from "react";

// type StateSetter<T> = (value: T | ((value: T) => T)) => void;
type ContextProps = {
  counter : number,
  setCounter: Dispatch<SetStateAction<number>>         // StateSetter<number>
}

const CounterContext: Context<Partial<ContextProps>> = createContext<Partial<ContextProps>>({});

export const CounterProvider: FC = ({children}) => {
  const [counter, setCounter] = useState(1);
  const props = {
    counter, setCounter
  } as ContextProps;
  return (
    <CounterContext.Provider value= {props}>
      {children}
    </CounterContext.Provider>
  );
}

export const useCounter = () : ContextProps => useContext(CounterContext) as ContextProps;