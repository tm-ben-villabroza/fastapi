import {
  ReactNode,
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";

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

  useEffect(() => {
    const authDataRaw = localStorage.getItem("auth");
    if (!authDataRaw) return;

    const authData = JSON.parse(authDataRaw);
    console.log(authData);
    setEmail(authData.email);
    setIsLoggedin(authData.isLoggedin);
  }, []);

  const login = (email: string) => {
    setEmail(email);
    setIsLoggedin(true);
    localStorage.setItem("auth", JSON.stringify({ email, isLoggedin: true }));
  };

  const logout = () => {
    setEmail("");
    setIsLoggedin(false);
    localStorage.setItem(
      "auth",
      JSON.stringify({ email: "", isLoggedin: false })
    );
  };

  const value = {
    email,
    isLoggedin,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
