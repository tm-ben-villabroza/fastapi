import { ReactNode, createContext, useContext, useState } from "react";

type AuthType = {
  isLoggedin: boolean;
  email: string;
  login: (email: string) => void;
  logout: () => void;
};

const initialAuthValues: AuthType = {
  isLoggedin: false,
  email: "",
  login: (email: string) => {},
  logout: () => {},
};

const AuthContext = createContext<AuthType>(initialAuthValues);

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [email, setEmail] = useState<string>("");
  const [isLoggedin, setIsLoggedin] = useState<boolean>(false);

  const login = (email: string) => {
    setEmail(email);
    setIsLoggedin(true);
  };

  const logout = () => {
    setEmail("");
    setIsLoggedin(false);
  };

  const value = {
    email,
    isLoggedin,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
