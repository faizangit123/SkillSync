import React from 'react';
import { Helmet } from 'react-helmet-async';

interface SEOProps {
  title?: string;
  description?: string;
  keywords?: string;
  type?: string;
  name?: string;
  image?: string;
}

export const SEO: React.FC<SEOProps> = ({
  title = 'SkillSync — Developer Growth Platform',
  description = 'Track your technical skills, manage projects, complete milestones, and accelerate your developer growth with SkillSync.',
  keywords = 'skill tracker, developer portfolio, project management, developer tools, coding progress, software engineering, MD Faizan',
  type = 'website',
  name = 'SkillSync',
  image = 'https://github.com/user-attachments/assets/8ca5976d-0860-47dd-9988-a20e8fd03c88',
}) => {
  return (
    <Helmet>
      {/* Standard metadata tags */}
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta name="keywords" content={keywords} />

      {/* Facebook tags */}
      <meta property="og:type" content={type} />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:site_name" content={name} />
      <meta property="og:image" content={image} />

      {/* Twitter tags */}
      <meta name="twitter:creator" content="@faizangit123" />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content={image} />
    </Helmet>
  );
};
