import Image from "next/image";
import { MagicCard } from "@/components/magicui/magic-card";

export default function Login() {
  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <MagicCard>
        <div className="p-4">
          <p>Hello World</p>
          <span>Hover me</span>
        </div>
      </MagicCard>
    </div>
  );
}
