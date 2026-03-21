import Image from "next/image";
import Link from "next/link";

const Logo: React.FC = () => {
  return (
    <Link href="/">
      <Image
        src="/gk & a logo.png"
        alt="GK&A Logistics Logo"
        width={80}
        height={25}
        quality={100}
        className=""
      />
    </Link>
  );
};

export default Logo;