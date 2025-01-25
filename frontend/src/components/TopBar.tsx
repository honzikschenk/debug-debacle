import { Button } from "./ui/button";

const TopBar = () => {
  return (
    <nav className="h-12 w-full text-white bg-slate-800 flex justify-between items-center px-5">
      <div>
        <h1>Test</h1>
      </div>
      <div>
        <Button>Button</Button>
      </div>
    </nav>
  )
}

export default TopBar;