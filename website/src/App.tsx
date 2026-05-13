import './App.css'
import statueHero from './assets/statue01.jpg'
import statueTwo from './assets/statue02.jpg'
import saadPark from './assets/saad_park1.jpg'
import saadParkTwo from './assets/saad_park2.jpg'
import church from './assets/outside_church.png'
import bebot from './assets/bebot_millas.png'
import katunggan from './assets/katunggan.png'
import homeMenu from './assets/home_menu.png'

const windowsDownload = 'https://ysxiaixsy.github.io/Nadumduman-1.0-web/'
const androidDownload =
  'https://github.com/dejely/Nadumduman/releases/latest/download/nadumduman-android.apk'

const navLinks = [
  ['Home', '#home'],
  ['About', '#about'],
  ['Features', '#features'],
  ['Screenshots', '#screenshots'],
  ['Download', '#download'],
  ['Community', '#community'],
] as const

const features = [
  {
    title: 'Explore Meaningful Places',
    text: 'Wander through Leganes landmarks inspired by real community spaces and hidden corners.',
    image: statueTwo,
    alt: 'Balintawak monument in the plaza',
  },
  {
    title: 'Collect Memories',
    text: 'Follow keepsakes, places, and moments that slowly bring the past back into focus.',
    image: saadPark,
    alt: 'Saad Park grounds',
  },
  {
    title: 'Meet Community Characters',
    text: 'Talk with locals, build connections, and uncover the stories held by the town.',
    image: bebot,
    alt: 'Bebot and Milla talabahan',
  },
  {
    title: 'Uncover Stories',
    text: 'Piece together the choices and promises that shape your journey through Nadumduman.',
    image: katunggan,
    alt: 'Katunggan Eco Park mangrove path',
  },
] as const

const screenshots = [
  { image: homeMenu, alt: 'Nadumduman home screen map' },
  { image: church, alt: 'Leganes Church scene' },
  { image: statueHero, alt: 'Balintawak statue scene' },
  { image: saadParkTwo, alt: 'Saad Park market scene' },
  { image: bebot, alt: 'Bebot and Milla restaurant scene' },
  { image: katunggan, alt: 'Katunggan Eco Park scene' },
] as const

type IconName =
  | 'android'
  | 'book'
  | 'download'
  | 'map'
  | 'play'
  | 'spark'
  | 'users'
  | 'windows'

type IconProps = {
  name: IconName
  className?: string
}

function Icon({ name, className = '' }: IconProps) {
  const common = {
    className: `icon ${className}`.trim(),
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: 1.8,
    strokeLinecap: 'round' as const,
    strokeLinejoin: 'round' as const,
    'aria-hidden': true,
  }

  switch (name) {
    case 'android':
      return (
        <svg {...common}>
          <path d="M7.5 9.5h9a1.8 1.8 0 0 1 1.8 1.8v5.2a2 2 0 0 1-2 2H7.7a2 2 0 0 1-2-2v-5.2a1.8 1.8 0 0 1 1.8-1.8Z" />
          <path d="M8 9.5 5.8 6.8" />
          <path d="m16 9.5 2.2-2.7" />
          <path d="M9 18.5v2" />
          <path d="M15 18.5v2" />
          <path d="M9 13h.01" />
          <path d="M15 13h.01" />
        </svg>
      )
    case 'book':
      return (
        <svg {...common}>
          <path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5Z" />
          <path d="M4 5.5A2.5 2.5 0 0 1 6.5 8H20" />
          <path d="M8 12h7" />
          <path d="M8 15h5" />
        </svg>
      )
    case 'download':
      return (
        <svg {...common}>
          <path d="M12 3v11" />
          <path d="m7 10 5 5 5-5" />
          <path d="M5 20h14" />
        </svg>
      )
    case 'map':
      return (
        <svg {...common}>
          <path d="m9 18-5 2V6l5-2 6 2 5-2v14l-5 2Z" />
          <path d="M9 4v14" />
          <path d="M15 6v14" />
        </svg>
      )
    case 'play':
      return (
        <svg {...common}>
          <path d="M8 5.5v13l11-6.5Z" />
        </svg>
      )
    case 'spark':
      return (
        <svg {...common}>
          <path d="M12 3 9.8 9.8 3 12l6.8 2.2L12 21l2.2-6.8L21 12l-6.8-2.2Z" />
        </svg>
      )
    case 'users':
      return (
        <svg {...common}>
          <path d="M16 20v-1.6c0-1.8-1.5-3.4-3.4-3.4H7.4C5.5 15 4 16.6 4 18.4V20" />
          <path d="M10 11a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Z" />
          <path d="M20 20v-1.4a3.2 3.2 0 0 0-2.4-3.1" />
          <path d="M15.8 4.3a3.5 3.5 0 0 1 0 6.4" />
        </svg>
      )
    case 'windows':
      return (
        <svg {...common}>
          <path d="m3 5.5 7.5-1v7H3Z" />
          <path d="m21 3-8.5 1.2v7.3H21Z" />
          <path d="M3 13h7.5v7L3 18.5Z" />
          <path d="M12.5 13H21v8l-8.5-1.2Z" />
        </svg>
      )
  }
}

function App() {
  return (
    <div className="site-page">
      <header className="site-header" aria-label="Primary navigation">
        <a className="brand" href="#home" aria-label="Nadumduman home">
          <span>Nadumduman</span>
        </a>
        <nav className="nav-links" aria-label="Page sections">
          {navLinks.map(([label, href]) => (
            <a key={href} href={href}>
              {label}
            </a>
          ))}
        </nav>
        <a className="button button-small button-primary header-cta" href="#download">
          <Icon name="download" />
          Download Now
        </a>
      </header>

      <main>
        <section className="hero-section" id="home">
          <div className="paper-edge paper-edge-left" aria-hidden="true" />
          <div className="hero-copy">
            <p className="eyebrow">A story-driven adventure game</p>
            <h1>
              Relive the Past.
              <span>Play the Story.</span>
            </h1>
            <p className="hero-description">
              Nadumduman is a heartfelt narrative adventure where you explore
              meaningful places, uncover memories, and experience the stories
              that shape a community.
            </p>
            <div className="hero-actions" aria-label="Primary actions">
              <a className="button button-primary" href="#download">
                <Icon name="download" />
                Download Now
              </a>
              <a className="button button-outline" href="#screenshots">
                <Icon name="play" />
                Watch Trailer
              </a>
            </div>
          </div>

          <div className="hero-art" aria-label="Artwork from Nadumduman">
            <img className="hero-main-image" src={statueHero} alt="Balintawak monument and plaza in Leganes" />
            <div className="postmark" aria-hidden="true">
              <span>Nadumduman</span>
              <span>Leganes</span>
            </div>
            <p className="hand-note">Our past, our pride, our home.</p>
            <figure className="polaroid polaroid-front">
              <img src={saadPark} alt="Saad Park in Leganes" />
            </figure>
            <figure className="polaroid polaroid-back">
              <img src={katunggan} alt="Katunggan Eco Park path" />
            </figure>
          </div>
        </section>

        <section className="section about-section" id="about" aria-labelledby="about-title">
          <div className="section-heading">
            <span className="rule" aria-hidden="true" />
            <p>Available on</p>
            <span className="rule" aria-hidden="true" />
          </div>
          <h2 id="about-title">Start your journey on Android or Windows.</h2>
          <div className="platform-grid">
            <a className="platform-card" href={windowsDownload} download>
              <Icon name="windows" />
              <span>
                <strong>Windows</strong>
                <small>PC Version</small>
              </span>
              <Icon name="download" className="platform-download" />
            </a>
            <a className="platform-card" href={androidDownload} download>
              <Icon name="android" />
              <span>
                <strong>Android</strong>
                <small>Mobile Version</small>
              </span>
              <Icon name="download" className="platform-download" />
            </a>
          </div>
        </section>

        <section className="section" id="features" aria-labelledby="features-title">
          <div className="section-heading">
            <span className="rule" aria-hidden="true" />
            <p>Game features</p>
            <span className="rule" aria-hidden="true" />
          </div>
          <h2 id="features-title">A quiet town story told through places.</h2>
          <div className="feature-grid">
            {features.map((feature) => (
              <article className="feature-card" key={feature.title}>
                <img src={feature.image} alt={feature.alt} />
                <div>
                  <h3>{feature.title}</h3>
                  <p>{feature.text}</p>
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="community-section" id="community" aria-labelledby="community-title">
          <div className="community-copy">
            <p className="eyebrow">Community and memory</p>
            <h2 id="community-title">Follow Renz through the places that remember him.</h2>
            <p>
              From Leganes Church to the mangrove paths of Katunggan, each stop
              carries a fragment of friendship, local culture, and a promise
              waiting to be remembered.
            </p>
          </div>
          <div className="community-stamps" aria-hidden="true">
            <span><Icon name="map" /> Leganes</span>
            <span><Icon name="users" /> Renz-kun</span>
            <span><Icon name="book" /> Memories</span>
            <span><Icon name="spark" /> Saad Festival</span>
          </div>
        </section>

        <section className="section screenshots-section" id="screenshots" aria-labelledby="screenshots-title">
          <div className="section-heading">
            <span className="rule" aria-hidden="true" />
            <p>In-game screenshots</p>
            <span className="rule" aria-hidden="true" />
          </div>
          <h2 id="screenshots-title">Scenes from the journey.</h2>
          <div className="screenshot-strip">
            {screenshots.map((shot) => (
              <img key={shot.alt} src={shot.image} alt={shot.alt} />
            ))}
          </div>
        </section>

        <section className="download-section" id="download" aria-labelledby="download-title">
          <div>
            <p className="eyebrow">Your story is waiting.</p>
            <h2 id="download-title">Download Nadumduman and begin the journey.</h2>
          </div>
          <div className="download-actions">
            <a className="button button-primary" href={windowsDownload} download>
              <Icon name="windows" />
              Windows ZIP
            </a>
            <a className="button button-outline" href={androidDownload} download>
              <Icon name="android" />
              Android APK
            </a>
          </div>
        </section>
      </main>
    </div>
  )
}

export default App
