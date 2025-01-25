import { Gamepad2, Link, Timer, User } from "lucide-react";
import { Button } from "./ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card";
import { NavLink } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";

interface NavbarProps {}

const Profile = () => {
  const { loginWithRedirect, user, isAuthenticated, logout, isLoading } =
    useAuth0();

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return isAuthenticated ? (
    <div>
      <HoverCard>
        <HoverCardTrigger asChild>
          <Button variant="link">
            <Avatar>
              <AvatarImage src={user.picture} />
              <AvatarFallback>{user.name.substring(0, 2)}</AvatarFallback>
            </Avatar>
          </Button>
        </HoverCardTrigger>
        <HoverCardContent className="w-80">
          <div className="flex justify-between space-x-4">
            <Avatar>
              <AvatarImage src={user.picture} />
              <AvatarFallback>{user.name.substring(0, 2)}</AvatarFallback>
            </Avatar>
            <div className="space-y-1">
              <h4 className="text-sm font-semibold">{user.name}</h4>
              <p className="text-sm">
                Thanks for trying out our project!
              </p>
            </div>
          </div>
        </HoverCardContent>
      </HoverCard>
      <Button
        onClick={() =>
          logout({ logoutParams: { returnTo: window.location.origin } })
        }
      >
        Log Out
      </Button>
    </div>
  ) : (
    <Button onClick={() => loginWithRedirect()}>Log In</Button>
  );
};

const Navbar = ({}: NavbarProps) => {
  return (
    <nav className="h-12 w-full text-white bg-slate-800 flex justify-between items-center px-5">
      <div className="flex items-center gap-x-10">
        <NavLink className="font-mono font-bold text-xl mr-5" to="/">
          Bug Fixer
        </NavLink>
      </div>
      <div className="flex items-center gap-x-2">
        <Profile />
      </div>
    </nav>
  );
};

export default Navbar;
